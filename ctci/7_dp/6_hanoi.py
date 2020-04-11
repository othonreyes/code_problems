def hanoi(n, ss, st, sa):
  if n == 1:
    st.append(ss.pop())
    return
  hanoi(n - 1, ss, sa, st)
  st.append(ss.pop())
  hanoi(n - 1, sa, st, ss)

if __name__ == "__main__":
  ss = [3,2,1]
  sa= []
  st = []
  hanoi(3, ss, st, sa)
  print(st)