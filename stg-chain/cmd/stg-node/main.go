package main

import (
	"flag"
	"fmt"
	"os"
	"time"
	"stg-chain/core"
	"stg-chain/network"
	"stg-chain/rpc"
)

func main() {
	genesisPath := flag.String("genesis", "core/genesis.json", "Path to genesis configuration")
	rpcPort := flag.Int("rpc.port", 8545, "RPC listening port")
	wsPort := flag.Int("ws.port", 8546, "WebSocket event streaming port")
	p2pAddr := flag.String("p2p.addr", "127.0.0.1:30303", "P2P network address binding socket")
	peerTarget := flag.String("peer", "", "Optional bootstrap connection target peer socket string")
	flag.Parse()

	fmt.Println("--------------------------------------------------")
	fmt.Println("STG SOVEREIGN MESH NODE INITIALIZATION")
	fmt.Println("--------------------------------------------------")

	if _, err := os.Stat(*genesisPath); err != nil {
		fmt.Printf("Genesis config missing error: %v\n", err)
		os.Exit(1)
	}

	stateStore := core.NewStateDB()
	rpc.SetStateStore(stateStore)

	// 📡 Initialize P2P Grid Interface Manager
	p2pManager := network.NewP2PManager(*p2pAddr, stateStore)
	go p2pManager.StartServer()

	// Connect to bootstrap peer node target configuration rules if specified
	if *peerTarget != "" {
		go func() {
			time.Sleep(1 * time.Second) // Small delay to let network stack settle
			p2pManager.ConnectToPeer(*peerTarget)
		}()
	}

	// ⏳ Upgraded Block Generation Loop with P2P Network Gossip Broadcast
	go func() {
		for {
			time.Sleep(3 * time.Second)
			stateStore.IncrementBlock()
			p2pManager.BroadcastBlock(stateStore.GetLatestBlock())
		}
	}()

	go rpc.StartWSServer(*wsPort, stateStore)
	rpc.StartRPCServer(*rpcPort)
}
