-- Create table for training data
CREATE TABLE IF NOT EXISTS train_data (
    id SERIAL PRIMARY KEY,
    cid INTEGER,
    time_feature INTEGER,
    trt INTEGER,
    age INTEGER,
    wtkg FLOAT,
    hemo INTEGER,
    homo INTEGER,
    drugs INTEGER,
    karnof INTEGER,
    oprior INTEGER,
    z30 INTEGER,
    zprior INTEGER,
    preanti INTEGER,
    race INTEGER,
    gender INTEGER,
    str2 INTEGER,
    strat INTEGER,
    symptom INTEGER,
    treat INTEGER,
    offtrt INTEGER,
    cd40 INTEGER,
    cd420 INTEGER,
    cd80 INTEGER,
    cd820 INTEGER
);

-- Create table for prediction results
CREATE TABLE IF NOT EXISTS predictions (
    id SERIAL PRIMARY KEY,
    pidnum INTEGER,
    cid INTEGER,
    time_feature INTEGER,
    trt INTEGER,
    age INTEGER,
    wtkg FLOAT,
    hemo INTEGER,
    homo INTEGER,
    drugs INTEGER,
    karnof INTEGER,
    oprior INTEGER,
    z30 INTEGER,
    zprior INTEGER,
    preanti INTEGER,
    race INTEGER,
    gender INTEGER,
    str2 INTEGER,
    strat INTEGER,
    symptom INTEGER,
    treat INTEGER,
    offtrt INTEGER,
    cd40 INTEGER,
    cd420 INTEGER,
    cd80 INTEGER,
    cd820 INTEGER,
    predicted INTEGER
);


-- Create table for new data results
CREATE TABLE IF NOT EXISTS new_data (
    id SERIAL PRIMARY KEY,
    pidnum INTEGER,
    cid INTEGER,
    time_feature INTEGER,
    trt INTEGER,
    age INTEGER,
    wtkg FLOAT,
    hemo INTEGER,
    homo INTEGER,
    drugs INTEGER,
    karnof INTEGER,
    oprior INTEGER,
    z30 INTEGER,
    zprior INTEGER,
    preanti INTEGER,
    race INTEGER,
    gender INTEGER,
    str2 INTEGER,
    strat INTEGER,
    symptom INTEGER,
    treat INTEGER,
    offtrt INTEGER,
    cd40 INTEGER,
    cd420 INTEGER,
    cd80 INTEGER,
    cd820 INTEGER,
    predicted INTEGER
);