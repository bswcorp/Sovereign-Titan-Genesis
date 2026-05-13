package core

import (
	"sync"
)

// StateDB manages the live state machine balances and block logs
type StateDB struct {
	mu       sync.RWMutex
	balances map[string]uint64
	latestBlk uint64
}

// NewStateDB initializes the database with pre-allocated accounts
func NewStateDB() *StateDB {
	db := &StateDB{
		balances: make(map[string]uint64),
		latestBlk: 777, // Default state height synchronization seed
	}
	
	// Alokasi Dana Awal Unit 008 ke Dompet Sultan Andi Muhammad Harpianto
	db.balances["0x3AA63941Fe0Ce029f4523c57A30C6dca3cB7343F"] = 1498000000000000000
	return db
}

// GetBalance returns the raw coin balance of an address
func (s *StateDB) GetBalance(address string) uint64 {
	s.mu.RLock()
	defer s.mu.RUnlock()
	return s.balances[address]
}

// SetBalance updates the state record for specific account
func (s *StateDB) SetBalance(address string, amount uint64) {
	s.mu.Lock()
	defer s.mu.Unlock()
	s.balances[address] = amount
}

// GetLatestBlock fetches the current runtime ledger tip
func (s *StateDB) GetLatestBlock() uint64 {
	s.mu.RLock()
	defer s.mu.RUnlock()
	return s.latestBlk
}

// IncrementBlock pushes the chain forward by 1 block
func (s *StateDB) IncrementBlock() {
	s.mu.Lock()
	defer s.mu.Unlock()
	s.latestBlk++
}
