{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python310
    pkgs.python310Packages.virtualenv
  ];

  shellHook = ''
    echo "Starting shell with Python 3.10..."

    # Create a virtual environment if it doesn't exist
    if [ ! -d venv ]; then
      echo "Creating a virtual environment..."
      ${pkgs.python310}/bin/python3.10 -m virtualenv venv
    fi

    # Activate the virtual environment
    echo "Activating the virtual environment..."
    source venv/bin/activate

    # Install dependencies from requirements.txt if it exists
    if [ -f requirements.txt ]; then
      echo "Installing dependencies from requirements.txt..."
      pip install -r requirements.txt
    else
      echo "requirements.txt not found, skipping dependency installation."
    fi
  '';
}
