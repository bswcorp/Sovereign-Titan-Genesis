package rpc

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"stg-chain/core"
)

type JSONRPCRequest struct {
	JSONRPC string        `json:"jsonrpc"`
	Method  string        `json:"method"`
	Params  []interface{} `json:"params"`
	ID      int           `json:"id"`
}

type JSONRPCResponse struct {
	JSONRPC string      `json:"jsonrpc"`
	Result  interface{} `json:"result,omitempty"`
	Error   interface{} `json:"error,omitempty"`
	ID      int         `json:"id"`
}

func StartRPCServer(port int, stateStore *core.StateDB) {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		w.Header().Set("Access-Control-Allow-Origin", "*")
		w.Header().Set("Access-Control-Allow-Methods", "POST, OPTIONS")
		w.Header().Set("Access-Control-Allow-Headers", "Content-Type")

		if r.Method == "OPTIONS" {
			w.WriteHeader(http.StatusOK)
			return
		}

		body, err := ioutil.ReadAll(r.Body)
		if err != nil {
			http.Error(w, "Failed to read request body", http.StatusBadRequest)
			return
		}

		var req JSONRPCRequest
		if err := json.Unmarshal(body, &req); err != nil {
			http.Error(w, "Invalid JSON", http.StatusBadRequest)
			return
		}

		var res JSONRPCResponse
		res.JSONRPC = "2.0"
		res.ID = req.ID

		switch req.Method {
		case "eth_blockNumber":
			// Menarik data langsung dari State Store dinamis
			res.Result = fmt.Sprintf("0x%x", stateStore.GetLatestBlock())
		case "eth_getBalance":
			if len(req.Params) > 0 {
				address := req.Params[0].(string)
				balance := stateStore.GetBalance(address)
				res.Result = fmt.Sprintf("0x%x", balance)
			} else {
				res.Error = "Missing address parameter"
			}
		default:
			res.Error = fmt.Sprintf("Method %s not implemented", req.Method)
		}

		json.NewEncoder(w).Encode(res)
	})

	addr := fmt.Sprintf(":%d", port)
	fmt.Printf("🚀 STG-Chain RPC server listening on %s\n", addr)
	http.ListenAndServe(addr, nil)
}
