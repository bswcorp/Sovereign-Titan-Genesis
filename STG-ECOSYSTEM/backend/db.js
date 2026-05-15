// 🗄️ STG UNIFIED - POSTGRESQL PERSISTENCE STORAGE LAYER
// Objective: Dynamic Ledger Indexing & Node Telemetry Tracking

const { Pool } = require('pg');
require('dotenv').config();

// Initialize connection pool parameters mapping to the secure baremetal instance
const pool = new Pool({
    connectionString: process.env.DATABASE_URL || "postgresql://postgres:postgres@localhost:5432/stg_unified"
});

// Automated table initialization schema
const initializeDatabaseSchema = async () => {
    const createTelemetryTable = `
        CREATE TABLE IF NOT EXISTS node_telemetry (
            id SERIAL PRIMARY KEY,
            node_id VARCHAR(50) NOT NULL,
            block_height VARCHAR(20) NOT NULL,
            recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    `;
    try {
        await pool.query(createTelemetryTable);
        console.log("💾 DATABASE: PostgreSQL telemetry schema verified and initialized.");
    } catch (err) {
        console.error("🚨 DB Core Error: Schema execution failed:", err.message);
    }
};

initializeDatabaseSchema();

module.exports = pool;
