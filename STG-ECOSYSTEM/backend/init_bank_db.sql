-- 🏛️ STG FINTECH HYBRID ECOSYSTEM DATABASE SYSTEM
-- Purpose: Relational Core Ledger Mapping Fiat Bank Accounts to Web3 Vault Wallets

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    associated_wallet VARCHAR(42) UNIQUE NOT NULL, -- Hooks into Web3 Layer
    kyc_status VARCHAR(20) DEFAULT 'PENDING',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS bank_accounts (
    account_number VARCHAR(20) PRIMARY KEY,
    user_id INT REFERENCES users(id),
    virtual_account_qris VARCHAR(50) UNIQUE NOT NULL,
    fiat_balance_idr NUMERIC(15, 2) DEFAULT 0.00,
    qubicoin_balance_qbc NUMERIC(36, 18) DEFAULT 0.000000000000000000,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS transaction_journal (
    tx_id VARCHAR(66) PRIMARY KEY, -- Can store standard 32-byte blockchain hashes
    sender_account VARCHAR(20),
    recipient_account VARCHAR(20),
    amount_fiat_idr NUMERIC(15, 2) DEFAULT 0.00,
    amount_crypto_qbc NUMERIC(36, 18) DEFAULT 0.000000000000000000,
    channel_type VARCHAR(20) NOT NULL, -- 'INTERNAL_TRANSFER', 'QRIS', 'VIRTUAL_ACCOUNT', 'METAPORTATION'
    status VARCHAR(20) DEFAULT 'SUCCESS',
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Seed Initial Entry for Andi Muhammad Harpianto (Sultan Account Layout)
INSERT INTO users (username, associated_wallet, kyc_status) 
VALUES ('Sultan_Andi_Harpinto', '0xf39fd6e51aad88f6f4ce6ab8827279cfffb92266', 'VERIFIED')
ON CONFLICT DO NOTHING;
