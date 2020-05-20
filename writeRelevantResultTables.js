const fs = require('fs')

const tables = JSON.parse(
  fs.readFileSync('./resultTables.json', 'utf8')
)

const relevantTables = tables.filter(
  (t) => t.result < -0.2 || t.result > 0.2
)

fs.writeFileSync(
  './relevantResultTables.json',
  JSON.stringify(relevantTables)
)
