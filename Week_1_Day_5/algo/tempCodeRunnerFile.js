  function zipArraysIntoMap(keys = [], values = []) {
    const hashMap = {};
  
    for (let i = 0; i < keys.length; i++) {
      const key = keys[i];
      const val = values[i];
  
      hashMap[key] = val;
    }
    return hashMap;
  }