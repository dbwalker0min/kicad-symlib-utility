#!/usr/bin/env python3
"""
Example usage of kicad-symlib-utility

This script demonstrates the basic functionality of the kicad-symlib-utility package.
"""

from pathlib import Path
from kicad_symlib_utility import KiCadSymbolLibrary

def main():
    # Example 1: Load and inspect a KiCad symbol library
    print("=== Loading KiCad Symbol Library ===")
    
    # Use the test data file as an example
    library_path = Path("tests/data/My_Resistor-0805.kicad_sym")
    
    if not library_path.exists():
        print(f"Error: Test file {library_path} not found!")
        return
    
    library = KiCadSymbolLibrary(library_path)
    
    print(f"KiCad version: {library.get_kicad_version()}")
    print(f"Number of symbols in library: {len(library.get_symbol_names())}")
    
    # Example 2: Get symbol properties
    print("\n=== Getting Symbol Properties ===")
    
    symbol_name = "1.5k"
    properties = library.get_symbol_properties(symbol_name)
    
    if properties:
        print(f"Properties for '{symbol_name}':")
        for prop_name, prop_value in properties.items():
            print(f"  {prop_name}: {prop_value}")
    else:
        print(f"Symbol '{symbol_name}' not found")
    
    # Example 3: Create a new derived symbol
    print("\n=== Creating New Derived Symbol ===")
    
    new_properties = {
        "Value": "1M",
        "Description": "1MΩ High precision resistor",
        "JLCPCB": "C123456",
        "ki_keywords": "r resistor precision"
    }
    
    try:
        library.derive_symbol_from("1M_precision", "~Template", new_properties)
        print(f"Successfully created new symbol '1M_precision'")
        
        # Verify the new symbol
        new_props = library.get_symbol_properties("1M_precision")
        print("Properties of new symbol:")
        for prop_name, prop_value in new_props.items():
            print(f"  {prop_name}: {prop_value}")
        
    except Exception as e:
        print(f"Error creating new symbol: {e}")
    
    # Example 4: Save the modified library
    print("\n=== Saving Modified Library ===")
    
    output_path = Path("/tmp/modified_library.kicad_sym")
    
    try:
        library.write_library(output_path)
        print(f"Library saved to: {output_path}")
        print(f"File size: {output_path.stat().st_size} bytes")
    except Exception as e:
        print(f"Error saving library: {e}")
    
    # Example 5: List all symbols (first 10)
    print("\n=== Symbol List (first 10) ===")
    
    all_symbols = library.get_symbol_names()
    for i, symbol_name in enumerate(all_symbols[:10]):
        derived_from = library.symbol_derived_from(symbol_name)
        if derived_from:
            print(f"  {symbol_name} (derived from {derived_from})")
        else:
            print(f"  {symbol_name} (template)")
    
    if len(all_symbols) > 10:
        print(f"  ... and {len(all_symbols) - 10} more symbols")

if __name__ == "__main__":
    main()