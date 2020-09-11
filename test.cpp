#include <unordered_map>
using namespace std;

class UF{
public:
    void connect(int a, int b){
        int a_gid = find(a);
        int b_gid = find(b);
        if(a_gid == b_gid){
            id_to_gid[a] = b_gid;
        }
    }

    int find(int id){
        if(id_to_gid.find(id) != id_to_gid.end()){
            id_to_gid[id] = id;
        }
        int t = id;
        while(id_to_gid[id] != id){
            id = id_to_gid[id];
        }
        while(id_to_gid[t] != t){
            t = id_to_gid[t];
            id_to_gid[t] = id;
        }
        return id;
    }
private:
    unordered_map<int, int> id_to_gid;    
};