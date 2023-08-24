'use strict';
const amphtmlValidator = require('amphtml-validator');
const axios = require('axios');
const fs = require('fs');
const he = require('he');

// amphtmlValidator.getInstance().then(function (validator) {
//   var result = validator.validateString('<html>Hello, world.</html>');
//   (result.status === 'PASS' ? console.log : console.error)(result.status);
//   for (var ii = 0; ii < result.errors.length; ii++) {
//     var error = result.errors[ii];
//     var msg =
//       'line ' + error.line + ', col ' + error.col + ': ' + error.message;
//     if (error.specUrl !== null) {
//       msg += ' (see ' + error.specUrl + ')';
//     }
//     (error.severity === 'ERROR' ? console.error : console.warn)(msg);
//   }
// })
(async function () {
    // let args = process.argv.slice(2)
    // let data = args[1]

    //process.stdout.write(argStr)
    // const req = await axios.get('https://food.detik.com/info-kuliner/d-6820681/rumput-laut-kering-di-resto-china-ternyata-dibuat-pakai-sayuran-ini/amp')
    // const data = req.data

    const pages = fs.readFileSync('amp.json')
    const pageJsons = JSON.parse(pages)

    const validator = await amphtmlValidator.getInstance()
    let results = []

    pageJsons.forEach((row) => {
        const url = row.url
        const content = he.decode(row.content)

        const result = validator.validateString(content)
        let status = result.status
        let message = ''

        result.errors.forEach((error, i) => {
            const specUrl = error.specUrl
            let msg = `line ${error.line}, col ${error.col}, : ${error.message}`

            if (specUrl !== null) {
                msg += `see ${specUrl}`
            }

            message += `${msg}\n`
        })

        results.push({
            url,
            status,
            message
        })
    })

    process.stdout.write(JSON.stringify(results))

})()