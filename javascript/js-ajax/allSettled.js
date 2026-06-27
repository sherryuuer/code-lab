const promise1 = new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve('Promise 1 resolved');
    }, 1000);
  });
  
  const promise2 = new Promise((resolve, reject) => {
    setTimeout(() => {
      reject('Promise 2 rejected');
    }, 1500);
  });
  
  const promise3 = new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve('Promise 3 resolved');
    }, 2000);
  });
  
  // Using Promise.allSettled to wait for all promises to settle
  Promise.allSettled([promise1, promise2, promise3])
    .then((results) => {
      console.log('All promises settled:', results);
      results.forEach((result, index) => {
        if (result.status === 'fulfilled') {
          console.log(`Promise ${index + 1} fulfilled with value:`, result.value);
        } else {
          console.log(`Promise ${index + 1} rejected with reason:`, result.reason);
        }
      });
    });

    
// not very useful one : any()
// Promise.any() resolves if any of the supplied promises is resolved.
