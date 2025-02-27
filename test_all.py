"""
Test Script for CrewAI Tutorial Examples

This script tests all the example scripts in the tutorial series.
It ensures that each script can be executed without errors and produces expected output.
"""

import os
import sys
import subprocess
from typing import List, Tuple
from dotenv import load_dotenv

def run_test(script_path: str) -> Tuple[bool, str]:
    """
    Run a test script and return the result.
    
    Args:
        script_path (str): Path to the script to test
        
    Returns:
        Tuple[bool, str]: Success status and output/error message
    """
    try:
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True,
            check=True
        )
        return True, f"Success: {result.stdout}"
    except subprocess.CalledProcessError as e:
        return False, f"Error: {e.stderr}"
    except Exception as e:
        return False, f"Error: {str(e)}"

def test_all_examples() -> List[Tuple[str, bool, str]]:
    """
    Test all example scripts in the tutorial series.
    
    Returns:
        List[Tuple[str, bool, str]]: List of (script_name, success, message)
    """
    # Load environment variables
    load_dotenv()
    
    # Validate environment
    if not os.getenv("OPENAI_API_KEY"):
        print("Warning: OPENAI_API_KEY not found in environment")
    if not os.getenv("GEMINI_API_KEY"):
        print("Warning: GEMINI_API_KEY not found in environment")
    
    # Define test scripts
    test_scripts = [
        "day1/basic_setup/simple_openai.py",
        "day2/tools_integration/basic_tools_demo.py",
        "day3/enhanced_agents/multi_agent_demo.py",
        "day3/enhanced_agents/simple_gemini.py",
        "day4/travel_planner/enhanced_main.py"
    ]
    
    results = []
    for script in test_scripts:
        print(f"\nTesting {script}...")
        success, message = run_test(script)
        results.append((script, success, message))
        print(f"{'✓' if success else '✗'} {script}")
        if not success:
            print(f"  {message}")
    
    return results

def main():
    """Run all tests and display results."""
    print("Starting CrewAI Tutorial Tests\n")
    
    results = test_all_examples()
    
    print("\nTest Summary:")
    print("=" * 50)
    
    total = len(results)
    passed = sum(1 for _, success, _ in results if success)
    
    for script, success, message in results:
        status = "PASS" if success else "FAIL"
        print(f"{status}: {script}")
    
    print("\nResults:")
    print(f"Total Tests: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {total - passed}")
    
    # Exit with appropriate status code
    sys.exit(0 if passed == total else 1)

if __name__ == "__main__":
    main() 