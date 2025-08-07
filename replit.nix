{ pkgs }:

pkgs.mkShell {
  buildInputs = [
    # Python and pip
    pkgs.python310
    pkgs.python310Packages.pip
    pkgs.python310Packages.virtualenv
    
    # Node.js and npm
    pkgs.nodejs-18_x
    pkgs.nodePackages.npm
    
    # Required system dependencies
    pkgs.zlib
    pkgs.libffi
    pkgs.openssl
  ];
  
  # Set environment variables
  shellHook = ''
    # Create and activate virtual environment
    if [ ! -d "venv" ]; then
      python -m venv venv
    fi
    source venv/bin/activate
    
    # Install Python dependencies
    if [ -f "backend/requirements.txt" ]; then
      pip install -r backend/requirements.txt
    fi
    
    # Install Node.js dependencies
    if [ -f "frontend/package.json" ]; then
      cd frontend && npm install
      cd ..
    fi
    
    export PYTHONPATH=$PYTHONPATH:$PWD/backend
    export FLASK_APP=backend/app.py
    export FLASK_ENV=development
  '';
}
