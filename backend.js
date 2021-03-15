const {Builder, By, Key, until} = require('selenium-webdriver');
(async function example() {
let driver = await new Builder().forBrowser("chrome").build();
try {
await driver.get('http://norvig.com/big.txt/');
await driver.findElement(By.name('q')).sendKeys('You did it!!', Key.RETURN);
await driver.wait(until.titleIs('You did it!! - Google Search'), 1000);
} finally {
await driver.quit();
}
})();