def LCS_top_down(A,B):
  na = len(A) # rows
  nb = len(B) # cols
  LCS = [[0 for i in range(nb + 1)] for _ in range(na + 1)]
  max = LCS_top_down_matrix(A, na, B, nb, LCS)
  return max, getLCSString(LCS)

def LCS_top_down_matrix(A, i, B, j, LCS):
  if i == 0 or j == 0:
    return 0
  if LCS[i][j] > 0:
    return LCS[i][j]

  if A[i-1] == B[j-1]:
    LCS[i][j] = 1 + LCS_top_down_matrix(A, i-1, B, j-1, LCS)
  else:
    LCS[i][j] = max(LCS_top_down_matrix(A, i-1, B, j, LCS), LCS_top_down_matrix(A, i, B, j-1, LCS))
  return LCS[i][j]


def LCS_bottom_up(A,B):
  na = len(A) # rows
  nb = len(B) # cols
  LCS = [[0 for i in range(nb + 1)] for _ in range(na + 1)]

  # +1 becasue we want to be able to find the value at a position n
  for i in range(1, na + 1):
    for j in range(1, nb + 1):
      if A[i-1] == B[j-1]:
        LCS[i][j] = 1 + LCS[i - 1][j - 1]
      else:
        LCS[i][j] = max(LCS[i - 1][j], LCS[i][j-1])
  for i in range(len(LCS)):
    print(LCS[i])

  return LCS[na][nb], getLCSString(LCS)

def getLCSString(LCS):
  # print the solution
  result = ""
  i = len(LCS) - 1
  j = len(LCS[0]) - 1
  
  while i>= 0 and j >=0 and LCS[i][j] > 0:
    # check if the diagonal cell has a smaller value
    if LCS[i-1][j-1] < LCS[i][j] and \
      LCS[i][j-1] < LCS[i][j] and \
      LCS[i-1][j] < LCS[i][j]:
      result += A[i-1]
      i -= 1
      j -= 1
    # check if top value has the same value as us
    if LCS[i-1][j] == LCS[i][j]:
      # if so then move to that cell
      i-=1
    # check if left value has the same value as us
    if LCS[i][j-1] == LCS[i][j]:
      # if so then move to that cell
      j-=1

  return result[::-1]
  

if __name__ == "__main__":
  A = "a"
  B = "a"
  print(LCS_bottom_up(A,B))
  A = "ac"
  B = "ab"
  print(LCS_bottom_up(A,B))

  A = "acbaed"
  B = "abcadf"
  print(LCS_bottom_up(A,B))

  A = "ABAZDC"
  B = "BACBAD"
  print(LCS_bottom_up(A,B))
  print("****" * 20)
  A = "a"
  B = "a"
  print(LCS_top_down(A,B))
  A = "ac"
  B = "ab"
  print(LCS_top_down(A,B))
  A = "acbaed"
  B = "abcadf"
  print(LCS_top_down(A,B))
  A = "ABAZDC"
  B = "BACBAD"
  print(LCS_top_down(A,B))