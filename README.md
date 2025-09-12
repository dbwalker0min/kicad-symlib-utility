# kicad-symlib-utility

A Python package for processing KiCad symbol libraries. This standalone package provides utilities for reading, manipulating, and writing KiCad symbol library files in S-expression format.

## Features

- **Load and parse** KiCad symbol library files (`.kicad_sym`) in S-expression format
- **Access and modify** symbol properties programmatically  
- **Create derived symbols** from template symbols with custom properties
- **Manage symbol inheritance** and template relationships
- **Write updated libraries** back to disk with proper formatting
- **Full error handling** with comprehensive validation

## Installation

Install using uv (recommended):

```bash
uv add kicad-symlib-utility
```

Or using pip:

```bash
pip install kicad-symlib-utility
```

## Quick Start

```python
from pathlib import Path
from kicad_symlib_utility import KiCadSymbolLibrary

# Load a KiCad symbol library
library = KiCadSymbolLibrary(Path("my_symbols.kicad_sym"))

# Get symbol properties
properties = library.get_symbol_properties("R_0805")
print(properties)

# Modify symbol properties
library.modify_properties("R_0805", {"Value": "10k", "Tolerance": "5%"})

# Create a new derived symbol from a template
new_properties = {
    "Value": "100k",
    "Tolerance": "1%", 
    "JLCPCB": "C25804"
}
library.derive_symbol_from("R_100k", "R_Template", new_properties)

# Save the modified library
library.write_library(Path("my_symbols_updated.kicad_sym"))
```

## API Reference

### KiCadSymbolLibrary

The main class for working with KiCad symbol libraries.

#### Constructor

```python
KiCadSymbolLibrary(symbol_file: Path, sexp: list | None = None)
```

- `symbol_file`: Path to the KiCad symbol library file
- `sexp`: Optional pre-parsed S-expression (for advanced use cases)

#### Key Methods

- `get_symbol_properties(symbol_name: str) -> dict[str, str] | None`: Get all properties for a symbol
- `modify_properties(symbol_name: str, new_properties: dict[str, str]) -> None`: Update symbol properties  
- `derive_symbol_from(new_name: str, template_name: str, properties: dict[str, str]) -> None`: Create derived symbol
- `delete_symbol(symbol_name: str) -> None`: Remove a symbol from the library
- `get_symbol_names() -> list[str]`: Get list of all symbol names
- `write_library(output_path: Path | None = None) -> None`: Save library to file

### KiCadVersionError

Exception raised for unsupported KiCad versions.

## Development

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

```bash
# Install development dependencies
uv sync --dev

# Run tests
uv run pytest

# Run linting
uv run ruff check
uv run ruff format

# Build package
uv build
```

## Requirements

- Python ≥ 3.12
- sexpdata ≥ 1.0.2

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
