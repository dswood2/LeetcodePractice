#include<iostream>
#include <vector>
#include <unordered_map>
#include<iterator>
using namespace std;
class Solution{
  public:
    vector<int> twoSum(vector<int>& nums, int target){
        unordered_map<int,int>mp;  //<value,index>
        vector<int>res;
        for(int i=0;i<nums.size();i++){
            if(mp.count(nums[i])){   //if number is found in map
                res.push_back(mp[nums[i]]);
                res.push_back(i);
                break;
            }
            mp[target-nums[i]]=i;
        }
        return res;
    }
};
int main(){
    Solution test;
    vector<int> sample;
    sample = {2,7,11,15};
    int sampleNum = 9; 
    vector<int>t=test.twoSum(sample,sampleNum);
    for(int i=0;i<t.size();i++){
        cout<<t[i]<<" ";
    }

}
