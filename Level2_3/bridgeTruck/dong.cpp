#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

class Truck {
public:
    int weight = 0;
    int sec = 0;
};
int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    
    vector<Truck> on_bridge; 
    vector<Truck> truck; 
    int on_weight = weight; 

    Truck t;
    for (int i = 0; i < truck_weights.size(); i++) {
        t.weight = truck_weights[i];
        truck.push_back(t);
    }
    
    for(int i=0;i<truck.size();i++) {
        while (true) {
            if (on_weight >= truck[i].weight) {
                on_bridge.push_back(truck[i]);
                on_weight -= truck[i].weight;
                answer++;
                for (int j = 0; j < on_bridge.size(); j++) {//다리 위 트럭들 sec++
                    on_bridge[j].sec++;
                    if (on_bridge[j].sec >= bridge_length) { //다 건넌 트럭은 pop
                        on_weight += on_bridge[j].weight;
                        on_bridge.erase(on_bridge.begin()); j--;
                    }
                }
                break;
            }
            else {
                for (int j = 0; j < on_bridge.size(); j++) {//다리 위 트럭들 sec++
                    on_bridge[j].sec++;
                    if (on_bridge[j].sec >= bridge_length) { //다 건넌 트럭은 pop
                        on_weight += on_bridge[j].weight;
                        on_bridge.erase(on_bridge.begin()); j--;
                    }
                }
            }answer++;
        }
    }
    answer += bridge_length;

    return answer;
}
int main() {
    vector<int> truck_weights = { 7,4,5,6 };
    cout<< solution(2, 10, truck_weights);
    cout << solution(100, 100, { 10 });
}