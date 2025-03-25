import subprocess
import time

# All the pytest combinations
combinations = [
    "python -m pytest -n auto --dist load",
    "python -m pytest -n auto --dist no",
    "python -m pytest -n 1 --dist load",
    "python -m pytest -n 1 --dist no",
    "python -m pytest --parallel-threads auto",
    "python -m pytest --parallel-threads 1",
    "python -m pytest -n auto --parallel-threads auto",
    "python -m pytest -n auto --parallel-threads 1",
    "python -m pytest -n 1 --parallel-threads auto",
    "python -m pytest -n 1 --parallel-threads 1",
    "python -m pytest -n auto --dist load --parallel-threads auto",
    "python -m pytest -n auto --dist load --parallel-threads 1",
    "python -m pytest -n auto --dist no --parallel-threads auto",
    "python -m pytest -n auto --dist no --parallel-threads 1",
    "python -m pytest -n 1 --dist load --parallel-threads auto",
    "python -m pytest -n 1 --dist load --parallel-threads 1",
    "python -m pytest -n 1 --dist no --parallel-threads auto",
    "python -m pytest -n 1 --dist no --parallel-threads 1"
]

# Extract the last 8 combinations
repeated_combinations = combinations[-8:]

# Log file setup
log_file = "pytest_parallel_results.log"
with open(log_file, "w") as log:
    log.write("Pytest Parallelization Experiment Results\n")
    log.write("=" * 50 + "\n")

# Run the first 10 combinations once
for combo in combinations[:-8]:
    print(f"Running: {combo}")
    with open(log_file, "a") as log:
        log.write(f"\nCOMMAND: {combo}\n")
        
        # Start timer
        start_time = time.time()
        
        # Run the command
        result = subprocess.run(combo, shell=True, capture_output=True, text=True)
        
        # Measure time and capture output
        duration = time.time() - start_time
        log.write(result.stdout)
        log.write(result.stderr)
        log.write(f"Execution Time: {duration:.2f} seconds\n")
        log.write("-" * 50 + "\n")
    
    print(f"✅ Finished: {combo}")

# Run the last 8 combinations three times each
for i in range(1, 4):
    for combo in repeated_combinations:
        print(f"Running: {combo} — Attempt {i}")
        with open(log_file, "a") as log:
            log.write(f"\nATTEMPT {i}: COMMAND: {combo}\n")
            
            # Start timer
            start_time = time.time()
            
            # Run the command
            result = subprocess.run(combo, shell=True, capture_output=True, text=True)
            
            # Measure time and capture output
            duration = time.time() - start_time
            log.write(result.stdout)
            log.write(result.stderr)
            log.write(f"Execution Time: {duration:.2f} seconds\n")
            log.write("-" * 50 + "\n")
        
        print(f"✅ Finished: {combo} — Attempt {i}")

print("\n🎉 All combinations tested! Check 'pytest_parallel_results.log' for details.")
