def solution(snapshots, transactions):

    visit_lst = [0] * 100001

    while transactions:
        count = 0
        if visit_lst[int(transactions[0][0])] == 0:
            visit_lst[int(transactions[0][0])] = 1
            if transactions[0][1] == "SAVE":
                for i in range(len(snapshots)):
                    if snapshots[i][0] == transactions[0][2]:
                        snapshots[i][1] = str(int(snapshots[i][1]) + int(transactions[0][3]))
                        transactions.pop(0)
                        count = 1
                        break
                if count == 0:
                    snapshots.append([transactions[0][2], transactions[0][3]])
                    transactions.pop(0)


            if transactions[0][1] == "WITHDRAW" and count ==0:
                for i in range(len(snapshots)):
                    if snapshots[i][0] == transactions[0][2]:
                        snapshots[i][1] = str(int(snapshots[i][1]) - int(transactions[0][3]))
                        transactions.pop(0)
                        break
        else:
            transactions.pop(0)


    return snapshots



snapshots = [
  ["ACCOUNT1", "100"],
  ["ACCOUNT2", "150"]
]

transactions = [
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["2", "WITHDRAW", "ACCOUNT1", "50"],
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["4", "SAVE", "ACCOUNT3", "500"],
  ["3", "WITHDRAW", "ACCOUNT2", "30"]
]

solution(snapshots, transactions)