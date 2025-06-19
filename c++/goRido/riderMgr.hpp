#pragma once

#include "rider.hpp"
#include <mutex>
using namespace std;


class RiderMgr {
	RiderMgr(){}
	static RiderMgr* riderMgrInstance;
	static mutex mtx;
	unordered_map<string, Rider*> ridersMap;
public:
	static RiderMgr* getRiderMgr();
	void addRider(string pRiderName, Rider* pRider);
	Rider* getRider(string pRiderName);
};