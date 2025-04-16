from tronpy import Tron

client = Tron()


def get_wallet_info(address: str):
    acc = client.get_account(address)
    resources = client.get_account_resource(address)

    balance = str(acc.get("balance", 0) / 1_000_000)
    bandwidth = str(resources.get("free_net_limit", 0))
    energy = str(resources.get("EnergyLimit", 0))

    return {
        "balance": balance,
        "bandwidth": bandwidth,
        "energy": energy
    }
