package core

import (
	"crypto/sha256"
	"encoding/hex"
	"fmt"
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
	CurrentBlock uint64
	Balances     map[string]uint64
	Transactions []Transaction
	CipherMap    map[string]string
}

func NewStateDB() *StateDB {
	s := &StateDB{
		CurrentBlock: 1,
		Balances:     make(map[string]uint64),
		Transactions: []Transaction{},
		CipherMap:    make(map[string]string),
	}

	s.Balances["0xgenesis"] = 1000000

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

	return s
}

func (s *StateDB) EncryptStringToAksara(input string) string {
	upper := strings.ToUpper(input)

	var out []string

	for _, c := range upper {
		v, ok := s.CipherMap[string(c)]

		if ok {
			out = append(out, v)
		} else {
			out = append(out, string(c))
		}
	}

	return strings.Join(out, "")
}

func (s *StateDB) IncrementBlock() {
	s.mu.Lock()
	defer s.mu.Unlock()

	s.CurrentBlock++
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

func (s *StateDB) SendTransaction(from, to string, value uint64) (string, error) {
	s.mu.Lock()
	defer s.mu.Unlock()

	if s.Balances[from] < value {
		return "", fmt.Errorf("insufficient funds")
	}

	s.Balances[from] -= value
	s.Balances[to] += value

	raw := fmt.Sprintf(
		"%s:%s:%d:%d",
		from,
		to,
		value,
		time.Now().UnixNano(),
	)

	hash := sha256.Sum256([]byte(raw))

	txHash := "0x" + hex.EncodeToString(hash[:])

	tx := Transaction{
		Hash:  txHash,
		From:  from,
		To:    to,
		Value: value,
	}

	s.Transactions = append(s.Transactions, tx)

	return txHash, nil
}

func (s *StateDB) GetTransactions() []Transaction {
	s.mu.RLock()
	defer s.mu.RUnlock()

	return s.Transactions
}
