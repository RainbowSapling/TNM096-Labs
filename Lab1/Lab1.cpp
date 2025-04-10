#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <time.h>

using namespace std;

vector<int> goalState = {1, 2, 3, 4, 5, 6, 7, 8, 0};

vector<int> startState1 = {2, 1, 7, 0, 4, 8, 3, 6, 5};

vector<int> startState2 = {7, 2, 4, 5, 0, 6, 8, 3, 1};

vector<int> startState3 = {5, 8, 4, 0, 7, 1, 3, 6, 2};

vector<int> startState4 = {0, 8, 3, 1, 7, 6, 2, 4, 5};

vector<int> startState5 = {8, 6, 7, 2, 5, 4, 3, 0, 1}; // Most difficult 8-puzzle


// h1 heuristic, find every tile that doesn't match the goal state
int calculateMisplaced(const vector<int>& state){
    int num = 0;

    for(int i=0; i < 9; i++){
        if(state[i] != goalState[i] && state[i] != 0){
            num++;
        }
    }

    return num;
}

//h2 heuristic
int calculateManhattan(const vector<int>& state){
    int sum = 0;

    for(int i=0; i < 9; i++){
        // Hole doesn't count
        if(state[i] != 0){
            int startRow = floor(i / 3);
            int startCol = i % 3;
            int goalRow = floor((state[i] - 1) / 3);
            int goalCol = (state[i] - 1) % 3;

            sum += abs(startRow - goalRow) + abs(startCol - goalCol);
        }
    }

    return sum;
}

struct StateNode {
    vector<int> state;
    int cost;
    
    // Default constructor
    StateNode(){}

    // Constructor
    StateNode(const vector<int>& state, int cost)
        : state(state), cost(cost) {}

    // Comparison operator that comapre nodes f=c+h values
    bool operator<(const StateNode& compare) const {
        // Priorty queue sort by largest first, flip comparison to get smallest fist
        //return cost + calculateMisplaced(state) > compare.cost + calculateMisplaced(compare.state); // h1
        return cost + calculateManhattan(state) > compare.cost + calculateManhattan(compare.state); // h2
    }

};

// Print function 
void printState(vector<int>& state){
    for(int i = 0; i < state.size(); i++){
        cout << state[i];
    }
    cout << "\n";
}

// Finds the position of the zero in a state
int findZeroPos(vector<int>& state){
    for(int i=0; i < 9; i++){
        if(state[i] == 0){
            return i;
        }
    }
}

// Find all possible moves from the current state
vector<int> findPossibleMoves(vector<int>& state){
    vector<int> possibleMoves;

    //Find where the zero is in the state
    int zeroPos = findZeroPos(state);

    // The position of the zero determines which moves are possible
    switch(zeroPos)
    {
    case 0:
        possibleMoves = {1,3};
        break;
    case 1:
        possibleMoves = {0,2,4};
        break;
    case 2:
        possibleMoves = {1,5};
        break;
    case 3:
        possibleMoves = {0,4,6};
        break;
    case 4:
        possibleMoves = {1,3,5,7};
        break;
    case 5:
        possibleMoves = {2,4,8};
        break;
    case 6:
        possibleMoves = {3,7};
        break;
    case 7:
        possibleMoves = {4,6,8};
        break;
    case 8:
        possibleMoves = {5,7};
        break;

    default:
        break;
    }

    return possibleMoves;
}

// Perform a move and return the new state
vector<int> makeMove(vector<int> state, int move){

    int zeroPos = findZeroPos(state);

    // A move consists of swapping the empty space with a surrounding tile, aka swap 0 with the number at the position of the move
    swap(state[zeroPos], state[move]);

    return state;
}

void aStar(vector<int> state){

    // Create a priority queue, since they automatically sort
    // Priority queue nomaly sorts largest first, but this is reversed from PuzzleStates comparison function, which gives best solutions at the front
    priority_queue<StateNode> openList;
    
    // Add start state with cost 0
    openList.emplace(state, 0);

    set<vector<int>> visitedStates;

    vector<int> possibleMoves;

    StateNode currentState;

    StateNode tempState;

    while(!openList.empty()){
        
        // Select current state and remove from openList
        currentState = openList.top();
        openList.pop();

        // When the goal is found -> stop
        if(currentState.state == goalState){
            cout << "Solution found!!\n";
            printState(currentState.state);
            cout << "Cost: " << currentState.cost;
            return;
        }

        // If state has been visited -> continue
        if(visitedStates.find(currentState.state) != visitedStates.end()){
            continue;
        }

        // Add current state to visited states
        visitedStates.insert(currentState.state);

        // Find the possible moves from the current state
        possibleMoves = findPossibleMoves(currentState.state);

        // Create new states from the possible moves, add unique ones to openList
        for(int i = 0; i < possibleMoves.size(); i++){
            tempState.state = makeMove(currentState.state, possibleMoves[i]);
            tempState.cost = currentState.cost + 1;
            
            // If tempState hasn't been visited -> add to openList
            if(visitedStates.find(tempState.state) == visitedStates.end()){
                openList.push(tempState);
            }
        }
    } 

    // Write out if there aren't any solutions
    cout << "No solution found :(";
}

int main() {
    clock_t tStart = clock();

    cout << "-------------- start -----------------\n";
    aStar(startState5);
    printf("\nTime taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
}