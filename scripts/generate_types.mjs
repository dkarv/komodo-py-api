import { exec } from "child_process";
import { readFileSync, writeFileSync } from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

console.log("generating python types...");

const gen_command =
  "RUST_BACKTRACE=full typeshare . --lang=python --output-file=../komodo_api/types.py";

exec(gen_command, (error, _stdout, _stderr) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log("generated types using typeshare");
  fix_types();
  console.log("finished.");
});

function fixMongoDocument(input) {
  return input
    .flatMap(line => 
      (line.includes('[MongoDocument]') || line.includes('[JsonObject]')) ? [
        '    model_config = ConfigDict(arbitrary_types_allowed=True)',
        line
      ] : [line]
    );
}

function moveToEndOfFile(lines, searchString) {
  const index = lines.findIndex(line => line.includes(searchString));
  if (index !== -1) {
    const [line] = lines.splice(index, 1);
    lines.push(line);
  }
}

function fix_types() {
  const types_path = __dirname + "/../komodo_api/types.py";
  const contents = readFileSync(types_path);
  var lines = contents
    .toString()
    // Replace number
    .replaceAll("I64 = number", 'I64 = int')
    .replaceAll("U64 = number", 'U64 = int')
    .replaceAll("Usize = number", 'Usize = int')
    // Wrong escape in comment
    .replaceAll('"\\^','"\\\\^')
    // IndexMap and IndexSet don't exist
    .replaceAll("from typing import Dict, Generic, List, Literal, Optional, TypeVar, Union",
      "from typing import Dict, Generic, List, Literal, Optional, TypeVar, Union, Mapping, Set, Any")
    .replaceAll("IndexMap", "Mapping")
    .replaceAll("IndexSet", "Set")
    .replaceAll("AlertDataVariant", "AlertDataTypes")
    .replaceAll("AlerterEndpointVariant", "AlerterEndpointTypes")
    .replaceAll("ResourceTargetVariant", "ResourceTargetTypes")
    .replaceAll("UserConfigVariant", "UserConfigTypes")
    .replaceAll("PathBuf", "str")
    .replaceAll(" = any", " = Any")
    .replaceAll("_for_:", "for_:")
    // TODO look into proper Partial
    .replace(/Partial\[(\w+)\]/g, '$1')
    .split("\n");

  moveToEndOfFile(lines, "_PartialAwsBuilderConfig = AwsBuilderConfig");
  moveToEndOfFile(lines, "_PartialServerBuilderConfig = ServerBuilderConfig");
  moveToEndOfFile(lines, "_PartialUrlBuilderConfig = UrlBuilderConfig");

  lines = fixMongoDocument(lines);

  writeFileSync(types_path, lines.join("\n"));
}
