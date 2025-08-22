# simple_agent.py
# UOMI Agent - Dani
# A simple example agent with placeholder logic for UOMI integration

import time

class UOMIAgent:
    def __init__(self, name, description, wallet):
        self.name = name
        self.description = description
        self.wallet = wallet
        self.running = False

    def on_start(self):
        print(f"🚀 Agent {self.name} is starting...")
        print(f"📝 {self.description}")
        print(f"💳 Wallet: {self.wallet}")
        self.running = True

    def handle_event(self, event):
        """
        Placeholder for handling events from UOMI.
        Replace this with actual UOMI API integration when available.
        """
        if event == "faucet_claim":
            print(f"🔔 {self.name} noticed someone claimed from the faucet!")
        elif event == "user_join":
            print(f"👋 {self.name} welcomes a new user to UOMI!")
        else:
            print(f"❓ {self.name} received an unknown event: {event}")

    def run(self):
        """
        Simulates a loop where the agent waits for events.
        In real deployment, this would be UOMI SDK or API callbacks.
        """
        self.on_start()
        events = ["user_join", "faucet_claim", "unknown_event"]

        for e in events:
            time.sleep(1)  # Simulate waiting for events
            self.handle_event(e)


# --- Agent Setup ---
AGENT_NAME = "Dani"
AGENT_DESCRIPTION = "An agent that welcomes users and tracks faucet claims"
AGENT_WALLET = "0x5da08546bff22a41b596424d454eb4191add0035"

# --- Run the Agent ---
if __name__ == "__main__":
    agent = UOMIAgent(AGENT_NAME, AGENT_DESCRIPTION, AGENT_WALLET)
    agent.run()
