const fs = require('fs')

const tables = JSON.parse(
  fs.readFileSync('./resultTables.json', 'utf8')
)

console.log('total amount of tables', tables.length)

const correspondingPatterns = {
  // linguistic
  AmorphousURI: 'TidyURI',
  ContextlessResource: 'ContextualisedResource',
  CRUDyURI: 'VerblessURI',
  NonHierarchicalNodes: 'HierarchicalNodes',
  PluralisedNodes: 'patternSingularisedPluralisedNodes',

  // design
  isIgnoringMIMEType: 'ContentNegotiation',
  isForgettingHypermedia: 'EntityLinking',
  isIgnoringCaching: 'ResponseCaching',
}

const relevantTables = tables
  .filter((t) => t.result < -0.2 || t.result > 0.2)
  .sort((a, b) => a.result < b.result)

console.log(
  'tables with significant result',
  relevantTables.length
)

const naTables = tables.filter((t) => t.result === 'NA')

console.log('tables with na', naTables.length)

fs.writeFileSync(
  './relevantResultTables.json',
  JSON.stringify(relevantTables)
)
