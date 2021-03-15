const {Builder, By, Key, until} = require('selenium-webdriver');
(async function example() {
let driver = await new Builder().forBrowser("chrome").build();
try {
    // navigate to entered url
await driver.get('http://norvig.com/big.txt/');
//
await driver.findElement(By.name('q')).sendKeys('You did it!!', Key.RETURN);
await driver.wait(until.titleIs('You did it!! - Google Search'), 1000);
} finally {
await driver.quit();
}
})();


// const {Builder, By, Key, until} = require('selenium-webdriver');

// (async function example() {
//     let driver = await new Builder().forBrowser('chrome').build();
//     try {
//         // Navigate to Url
//         await driver.get('https://www.google.com');

//         // Enter text "cheese" and perform keyboard action "Enter"
//         await driver.findElement(By.name('q')).sendKeys('cheese', Key.ENTER);

//         let firstResult = await driver.wait(until.elementLocated(By.css('h3>div')), 10000);

//         console.log(await firstResult.getAttribute('textContent'));
//     }
//     finally{
//         driver.quit();
//     }
// })();