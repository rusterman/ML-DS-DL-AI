If you are using an online Python IDE to run the `function-transformation.py` file, 
you may encounter a warning that typically appears when plotting with Matplotlib. 
This happens because Fontconfig cannot locate the font cache directory.
```bash
Fontconfig error: No writable cache directories
```

To resolve this, add the following lines of code to the top of the `.py` file before 
importing the project libraries to create a unique temporary cache folder. 
Consequently, programs relying on `XDG_CACHE_HOME` (such as Fontconfig, certain graphics libraries, etc.) 
will write their cache files to this temporary folder instead of the standard user directory:
```bash
import os
import tempfile

# Automatically creates a unique, writable folder inside /tmp
unique_cache_dir = tempfile.mkdtemp(prefix="fontconfig_")

# Set the environment variable
os.environ["XDG_CACHE_HOME"] = unique_cache_dir
```
