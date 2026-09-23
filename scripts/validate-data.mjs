import fs from 'node:fs';
import path from 'node:path';
import Ajv from 'ajv';
import addFormats from 'ajv-formats';

const ajv = new Ajv({ allErrors: true });
addFormats(ajv);
const eventSchema = JSON.parse(fs.readFileSync('schemas/event.schema.json', 'utf8'));
const yearSchema = JSON.parse(fs.readFileSync('schemas/year.schema.json', 'utf8'));
const validateEvent = ajv.compile(eventSchema);
const validateYear = ajv.compile(yearSchema);
const errors = [];
const ids = new Set();
let eventCount = 0;

for (let year = 1990; year <= 2026; year++) {
  const yearPath = `src/data/years/${year}.json`;
  const eventPath = `src/data/events/${year}.json`;
  if (!fs.existsSync(yearPath) || !fs.existsSync(eventPath)) {
    errors.push(`${year}: missing year or event file`);
    continue;
  }
  const yearData = JSON.parse(fs.readFileSync(yearPath, 'utf8'));
  const events = JSON.parse(fs.readFileSync(eventPath, 'utf8'));
  if (!validateYear(yearData)) errors.push(`${yearPath}: ${ajv.errorsText(validateYear.errors)}`);
  if (yearData.year !== year) errors.push(`${yearPath}: year does not match filename`);
  if (!Array.isArray(events)) {
    errors.push(`${eventPath}: expected an array`);
    continue;
  }
  const localIds = new Set();
  for (const event of events) {
    eventCount++;
    if (!validateEvent(event)) errors.push(`${eventPath} ${event.id ?? '?'}: ${ajv.errorsText(validateEvent.errors)}`);
    if (event.year !== year) errors.push(`${eventPath} ${event.id}: year does not match filename`);
    if (ids.has(event.id)) errors.push(`duplicate event ID: ${event.id}`);
    ids.add(event.id);
    localIds.add(event.id);
    if (event.image?.startsWith('/') && !fs.existsSync(path.join('public', event.image))) {
      errors.push(`${eventPath} ${event.id}: missing image ${event.image}`);
    }
  }
  for (const id of yearData.events ?? []) {
    if (!localIds.has(id)) errors.push(`${yearPath}: unknown event ID ${id}`);
  }
}

if (errors.length) {
  console.error(errors.join('\n'));
  process.exitCode = 1;
} else {
  console.log(`Validated 37 years and ${eventCount} events.`);
}
