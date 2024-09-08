#include <cstdlib>
#include <iostream>
#include <random>
#include <set>
#include <string>
#include <utility>
#include <vector>
std::vector<std::vector<int>> goal = {{1, 2, 3}, {4, 5, 6}, {7, 8, 0}};
inline int manhattandistance(std::vector<std::vector<int>> board);
inline std::vector<int> findzero(std::vector<std::vector<int>> board);
inline std::vector<std::vector<int>>
movetile(std::vector<std::vector<int>> board, char direction);
inline std::pair<std::vector<std::vector<std::vector<int>>>, int>
solve8puzzle(std::vector<std::vector<int>> board);
inline std::vector<std::vector<int>> generaterandomsolvableboard();
inline void solve8puzzle10000times();
int main() { solve8puzzle10000times(); }

inline int manhattandistance(std::vector<std::vector<int>> board) {
  using namespace std;
  int distance = 0;
  for (int i = 0; i < 3; i++)
    for (int j = 0; j < 3; j++)
      if (board[i][j] != 0) {
        int targetx = (board[i][j] - 1) / 3, targety = (board[i][j] - 1) % 3;
        distance += abs(i - targetx) + abs(j - targety);
      }
  return distance;
}

inline std::vector<int> findzero(std::vector<std::vector<int>> board) {
  using namespace std;
  for (int i = 0; i < 3; i++)
    for (int j = 0; j < 3; j++)
      if (board[i][j] == 0)
        return vector<int>({i, j});
}

inline std::vector<std::vector<int>>
movetile(std::vector<std::vector<int>> board, char direction) {
  using namespace std;
  auto tmp = findzero(board);
  int x0 = tmp[0], y0 = tmp[1];
  auto newboard = board;
  if (direction == 's' && x0 > 0)
    swap(newboard[x0][y0], newboard[x0 - 1][y0]);
  else if (direction == 'w' && x0 < 2)
    swap(newboard[x0][y0], newboard[x0 + 1][y0]);
  else if (direction == 'a' && y0 < 2)
    swap(newboard[x0][y0], newboard[x0][y0 + 1]);
  else if (direction == 'd' && y0 > 0)
    swap(newboard[x0][y0], newboard[x0][y0 - 1]);
  return newboard;
};

inline std::pair<std::vector<std::vector<std::vector<int>>>, int>
solve8puzzle(std::vector<std::vector<int>> board) {
  using namespace std;
  auto issolvable = [](vector<vector<int>> board) -> bool {
    int inversioncount = 0;
    vector<int> flatboard;
    flatboard.reserve(8);
    for (auto &i : board)
      for (int &j : i)
        if (j != '0')
          flatboard.push_back(j);
    for (int i = 0; i < 8; i++)
      for (int j = i + 1; j < 8; j++)
        if (flatboard[i] > flatboard[j])
          ++inversioncount;
    return inversioncount % 2 == 0;
  };
  if (!issolvable(board))
    return make_pair(vector<vector<vector<int>>>(), -1);
  using fourelement =
      pair<pair<int, int>,
           pair<vector<vector<int>>, vector<vector<vector<int>>>>>;
  set<fourelement> openlist;
  set<vector<vector<int>>> closedset;
  openlist.insert(make_pair(make_pair(manhattandistance(board), 0),
                            make_pair(board, vector<vector<vector<int>>>())));
  while (!openlist.empty()) {
    auto popedelement = *openlist.begin();
    openlist.erase(openlist.begin());
    auto _ = popedelement.first.first;
    auto cost = popedelement.first.second;
    auto currentboard = popedelement.second.first;
    auto path = popedelement.second.second;
    if (closedset.contains(currentboard))
      continue;
    closedset.insert(currentboard);
    if (currentboard == goal)
      return make_pair(path, path.size());
    string temp = "swad"s;
    for (char &direction : temp) {
      auto newboard = movetile(currentboard, direction);
      if (!closedset.contains(newboard)) {
        int newcost = cost + 1;
        auto newpath = path;
        newpath.push_back(newboard);
        openlist.insert(
            make_pair(make_pair(newcost + manhattandistance(newboard), newcost),
                      make_pair(newboard, newpath)));
      }
    }
  }
  return {vector<vector<vector<int>>>(), -1};
}

inline std::vector<std::vector<int>> generaterandomsolvableboard() {
  using namespace std;
  while (true) {
    vector<int> seed{0, 1, 2, 3, 4, 5, 6, 7, 8};
    random_device seedgen;
    mt19937 engine(seedgen());
    shuffle(seed.begin(), seed.end(), engine);
    vector<vector<int>> ret(3, vector<int>(3));
    for (int i = 0; i < 9; i++)
      ret[i / 3][i % 3] = seed[i];
    if (solve8puzzle(ret).second != -1)
      return ret;
  }
}

inline void solve8puzzle10000times() {
  using namespace std;
  for (int i = 0; i < 10000; i++) {
    cerr << "generating...\n";
    auto board = generaterandomsolvableboard();
    cerr << "generated!\n";
    auto a = solve8puzzle(board);
    cout << a.second << '\n';
  }
}
