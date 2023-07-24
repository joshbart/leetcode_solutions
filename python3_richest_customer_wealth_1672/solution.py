class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        most_wealth = 0
        for cust in range(len(accounts)):
            cust_wealth = 0
            for bank in range(len(accounts[cust])):
                bank_amount = accounts[cust][bank]
                cust_wealth += bank_amount
            if cust_wealth > most_wealth:
                most_wealth = cust_wealth
        return most_wealth