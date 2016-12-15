from __future__ import nested_scopes
from __future__ import generators
from __future__ import division
from __future__ import absolute_import
from __future__ import with_statement
from __future__ import print_function
from __future__ import unicode_literals

import ansible.runner
import sys

__author__ = "Sean Douglas"

def main():

	# construct the ansible runner and execute on all hosts
	results = ansible.runner.Runner(
	    pattern='*', forks=10,
	    module_name='command', module_args='/usr/bin/uptime',
	).run()
	
	if results is None:
	   print "No hosts found"
	   sys.exit(1)
	
	print "UP ***********"
	for (hostname, result) in results['contacted'].items():
	    if not 'failed' in result:
	        print "%s >>> %s" % (hostname, result['stdout'])
	
	print "FAILED *******"
	for (hostname, result) in results['contacted'].items():
	    if 'failed' in result:
	        print "%s >>> %s" % (hostname, result['msg'])
	
	print "DOWN *********"
	for (hostname, result) in results['dark'].items():
	    print "%s >>> %s" % (hostname, result)
	
if __name__ == "__main__":
	main()
