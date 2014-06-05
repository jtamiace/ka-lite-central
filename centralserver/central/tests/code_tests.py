from fle_utils.testing.code_testing import FLECodeTest

class CentralCodeTest(FLECodeTest):
    testable_packages = ['kalite', 'securesync', 'fle_utils.config', 'fle_utils.chronograph', 'fle_utils.deployments', 'fle_utils.feeds', 'centralserver']
