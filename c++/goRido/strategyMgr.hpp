#pragma once
#include "tripMetaData.hpp"
#include "ratingBasedPricingStrategy.hpp"
#include "leastTimeBasedMatchingStrategy.hpp"
#include "defaultPricingStrategy.hpp" 
#include "common.hpp"
#include "mutex"
using namespace std;

class StrategyMgr {
	StrategyMgr() {}
	static StrategyMgr* strategyMgrInstance;
	static mutex mtx;

public:
	static StrategyMgr* getStrategyMgr();
	PricingStrategy* determinePricingStrategy(TripMetaData* metaData);
	DriverMatchingStrategy* determineMatchingStrategy(TripMetaData* metaData);
};