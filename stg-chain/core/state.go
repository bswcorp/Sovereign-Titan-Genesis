package core

import (
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
	"strings"
	"sync"
	"time"
)

type Transaction struct {
	Hash  string `json:"hash"`
	From  string `json:"from"`
	To    string `json:"to"`
	Value uint64 `json:"value"`
}

type StateDB struct {
	mu           sync.RWMutex
	CurrentBlock uint64                 `json:"current_block"`
	Balances     map[string]uint64      `json:"balances"`
	Transactions []Transaction          `json:"transactions"`
	CipherMap    map[string]string      `json:"-"`
	dbPath       string                 `json:"-"`
}

func NewStateDB(dbPath string) *StateDB {
	s := &StateDB{
		CurrentBlock: 1,
		Balances:     make(map[string]uint64),
		Transactions: []Transaction{},
		CipherMap:    make(map[string]string),
		dbPath:       dbPath,
	}

	// Initialize Level 2 Aksara-Logic Encryption Matrix
	s.CipherMap["0"] = "꧐"
	s.CipherMap["1"] = "꧑"
	s.CipherMap["2"] = "꧒"
	s.CipherMap["3"] = "꧓"
	s.CipherMap["4"] = "꧔"
	s.CipherMap["5"] = "꧕"
	s.CipherMap["6"] = "꧖"
	s.CipherMap["7"] = "꧗"
	s.CipherMap["8"] = "꧘"
	s.CipherMap["9"] = "꧙"
	s.CipherMap["A"] = "ꦄ"
	s.CipherMap["B"] = "ꦧ"
	s.CipherMap["C"] = "ꦼ"
	s.CipherMap["D"] = "ꦢ"
	s.CipherMap["E"] = "ꦌ"
	s.CipherMap["X"] = "ꦏꦱ"

	// Attempt to load from persistent storage disk layer
	if err := s.loadFromDisk(); err != nil {
		// Default fallback allocation if storage file does not exist
		s.Balances["0xgenesis"] = 1000000
		s.saveToDisk()
	}

	return s
}

func (s *StateDB) loadFromDisk() error {
	if _, err := os.Stat(s.dbPath); os.IsNotExist(err) {
		return err
	}
	data, err := ioutil.ReadFile(s.dbPath)
	if err != nil {
		return err
	}
	return json.Unmarshal(data, s)
}

func (s *StateDB) saveToDisk() {
	data, _ := json.MarshalIndent(s, "", "  ")
	_ = ioutil.WriteFile(s.dbPath, data, 0644)
}

func (s *StateDB) EncryptStringToAksara(input string) string {
	upperInput := strings.ToUpper(input)
	var output []string
	for _, char := range upperInput {
		strChar := string(char)
		if val, exists := s.CipherMap[strChar]; exists {
			output = append(output, val)
		} else {
			output = append(output, strChar)
		}
	}
	return strings.Join(output, "")
}

func (s *StateDB) IncrementBlock() {
	s.mu.Lock()
	defer s.mu.Unlock()
	s.CurrentBlock++
	s.saveToDisk()
}

func (s *StateDB) GetBlock() uint64 {
	s.mu.RLock()
	defer s.mu.RUnlock()
	return s.CurrentBlock
}

func (s *StateDB) GetBalance(addr string) uint64 {
	s.mu.RLock()
	defer s.mu.RUnlock()
	return s.Balances[addr]
}

func (s *StateDB) SendTransaction(from string, to string, value uint64) (string, error) {
	s.mu.Lock()
	defer s.mu.Unlock()

	if s.Balances[from] < value {
		return "", fmt.Errorf("insufficient funds")
	}

	s.Balances[from] -= value
	s.Balances[to] += value

	raw := fmt.Sprintf("%s:%s:%d:%d", from, to, value, time.Now().UnixNano())
	hash := sha256.Sum256([]byte(raw))
	txHash := "0x" + hex.EncodeToString(hash[:])

	tx := Transaction{
		Hash:  txHash,
		From:  from,
		To:    to,
		Value: value,
	}

	s.Transactions = append(s.Transactions, tx)
	s.saveToDisk()
	return txHash, nil
}

func (s *StateDB) GetTransactions() []Transaction {
	s.mu.RLock()
	defer s.mu.RUnlock()
	return s.Transactions
}
