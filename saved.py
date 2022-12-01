"""An example of constructing a profile with a single raw PC.

Instructions:
Wait for the profile instance to start, and then log in to the host via the
ssh port specified below.
"""

import geni.portal as portal
import geni.rspec.pg as rspec

# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()
 
# Create a raw PC
node = request.RawPC("test-node")
node.addService(rspec.Execute(shell="bash", command="/local/repository/bin/package.sh"))

# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()
