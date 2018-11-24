# ocatling_fpl_tools
Experiemts with the fantasy API in Python

Wanted to try working with the Fantasy Premier League API, as I need to A) Learn to work with API's using python B) Drastically improve my team. 
Few Ideas for Tools largely around comparing gameweeks for players with better fixtures

TODO:
- Import data
  - getTeams : JSON
  - getTeam(id) : team
  - getFixtures : JSON
  - getFixture(id) : fixture
  - getPlayers : JSON
  - getPlayer(id) : player

- Console menu interface for tools

- Given number of future gameweeks calculate teams with best fixtures
  - getGWDifficulty : array[int]
  - total : int
  - orderByDifficulty :array[team]

- Suggest Players From Team
  - Get Players(team) : list<player>
  - SortByForm(list<players>) : list<players>

- Suggest Players From Team With Comparable Position
  - Get Position(player) : string
  - getPlayers(team) : list<player>
  - getPositionPlayers(string) : list<player>
