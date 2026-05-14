package core

import (
	"crypto/sha256"
	"encoding/hex"
	"errors"
	"fmt"
	"sync"
	"time"
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
	EventBus   chan Transaction // Phase 5: Real-time broadcast pipe
}

func NewStateDB() *StateDB {
	db := &StateDB{
		balances:   make(map[string]uint64),
		txRegistry: make([]Transaction, 0),
		latestBlk:  1,
		EventBus:   make(chan Transaction, 100),
	}
	// Initial Asset Reservation
	db.balances["0x3AA63941Fe0Ce029f4523c57A30C6dca3cB7343F"] = 100000000000000000
	return db
}

func (s *StateDB) GetBalance(address string) uint64 {
	s.mu.RLock()
	defer s.mu.RUnlock()
	return s.balances[address]
}

func (s *StateDB) SetBalance(address string, amount uint64) {
	s.mu.Lock()
	defer s.mu.Unlock()
	s.balances[address] = amount
}

func (s *StateDB) AddTransaction(from, to string, amount uint64) (string, error) {
	s.mu.Lock()
	defer s.mu.Unlock()

	if s.balances[from] < amount {
		return "", errors.New("insufficient balance inside sovereign core storage")
	}

	s.balances[from] -= amount
	s.balances[to] += amount

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
	
	// Phase 5 Broadcast: Fire event non-blockingly into the stream pipe
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
}

func (s *StateDB) GetLatestBlock() uint64 {
	s.mu.RLock()
	defer s.mu.RUnlock()
	return s.latestBlk
}
