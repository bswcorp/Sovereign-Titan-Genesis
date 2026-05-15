// STG Embedded Hardware Descriptor Blueprint
// Microprocessor & Encrypted Secure Enclave Flag Pins

#define SYSTEM_CHAIN_ID      777
#define CHIP_ARCHITECTURE    "ARM64_BAREMETAL"
#define ENCLAVE_KEY_SLOT     0x309
#define EMBEDDED_AI_ENABLED  1
#define HARDWARE_REVISION    "TITAN-M5-REV1"

// Signal lines connecting hardware telemetry to local Web5 protocol
const char* RPC_ENDPOINT = "http://localhost:8545";
