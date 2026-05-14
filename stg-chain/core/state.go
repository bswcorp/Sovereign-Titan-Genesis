package core

import (
	"crypto/sha256"
	"encoding/hex"
	"errors"
	"fmt"
	"sync"
	"time"
	
	"stg-chain/storage"
)

type Transaction struct {
	Hash      string `json:"hash"`
	From      string `json:"from"`
	To        string `json:"to"`
	Value     uint64 `json:"value"`
	Timestamp int64  `json:"timestamp"`
}

type StateDB struct {
	mu         sync.RWMutex
	balances   map[string]uint64
	txRegistry []Transaction
	latestBlk  uint64
	EventBus   chan Transaction
	diskStore  *storage.Store // Phase 8 Storage Connection
}

func NewStateDB() *StateDB {
	disk := storage.NewStore()
	db := &StateDB{
		balances:   make(map[string]uint64),
		txRegistry: make([]Transaction, 0),
		latestBlk:  1,
		EventBus:   make(chan Transaction, 100),
		diskStore:  disk,
	}
	
	// Seed Sovereign Architect allocations and write record to local storage disk
	sultanWallet := "0x3AA63941Fe0Ce029f4523c57A30C6dca3cB7343F"
	initialFunds := uint64(100000000000000000)
	db.balances[sultanWallet] = initialFunds
	db.diskStore.PutBalance(sultanWallet, initialFunds)
	
	return db
}

func (s *StateDB) GetBalance(address string) uint64 {
	s.mu.RLock()
	defer s.mu.RUnlock()
	return s.balances[address]
}

func (s *StateDB) AddTransaction(from, to string, amount uint64) (string, error) {
	s.mu.Lock()
	defer s.mu.Unlock()

	if s.balances[from] < amount {
		return "", errors.New("insufficient balance inside sovereign core storage")
	}

	s.balances[from] -= amount
	s.balances[to] += amount
	
	// Commit balances to LevelDB
	s.diskStore.PutBalance(from, s.balances[from])
	s.diskStore.PutBalance(to, s.balances[to])

	timestamp := time.Now().Unix()
	rawPayload := fmt.Sprintf("%s-%s-%d-%d", from, to, amount, timestamp)
	hashBytes := sha256.Sum256([]byte(rawPayload))
	txHash := "0x" + hex.EncodeToString(hashBytes[:])

	newTx := Transaction{
		Hash:      txHash,
		From:      from,
		To:        to,
		Value:     amount,
		Timestamp: timestamp,
	}

	s.txRegistry = append(s.txRegistry, newTx)
	
	select {
	case s.EventBus <- newTx:
	default:
	}

	return txHash, nil
}

func (s *StateDB) GetTransactions() []Transaction {
	s.mu.RLock()
	defer s.mu.RUnlock()
	return s.txRegistry
}

func (s *StateDB) IncrementBlock() {
	s.mu.Lock()
	defer s.mu.Unlock()
	s.latestBlk++
	
	// Archive the block event structurally down to disk
	blockMeta := map[string]interface{}{
		"number":    s.latestBlk,
		"timestamp": time.Now().Unix(),
		"tx_count":  len(s.txRegistry),
	}
	s.diskStore.PutBlock(s.latestBlk, blockMeta)
}

func (s *StateDB) GetLatestBlock() uint64 {
	s.mu.RLock()
	defer s.mu.RUnlock()
	return s.latestBlk
}
