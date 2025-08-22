# simple_agent.py
# UOMI Agent - Dani

class UOMIAgent:
    def __init__(self, name, description, wallet):
        self.name = name
        self.description = description
        self.wallet = wallet

    def on_start(self):
        print(f"🚀 Agent {self.name} is now running")
        print(f"📝 {self.description}")
        print(f"💳 Wallet: {self.wallet}")

    def on_event(self, event):
        if event == "faucet_claim":
            print(f"🔔 {self.name} noticed someone claimed from the faucet!")

# --- Agent Setup ---
AGENT_NAME = "Dani"
AGENT_DESCRIPTION = "An agent that welcomes users and tracks faucet claims"
AGENT_WALLET = "0x5da08546bff22a41b596424d454eb4191add0035"

# --- Run the Agent ---
if __name__ == "__main__":
    agent = UOMIAgent(AGENT_NAME, AGENT_DESCRIPTION, AGENT_WALLET)
    agent.on_start()

    # Example test event
    agent.on_event("faucet_claim")
