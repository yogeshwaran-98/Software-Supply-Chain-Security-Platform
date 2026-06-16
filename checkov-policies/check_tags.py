from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories


class RequiredTagsCheck(BaseResourceCheck):

    def __init__(self):
        name = "Ensure AWS resources have Owner, Environment, CostCenter tags"
        id = "CKV_CUSTOM_1"
        supported_resources = ["*"]
        categories = [CheckCategories.GOVERNANCE]
        super().__init__(name=name, id=id)

    def scan_resource_conf(self, conf):
        tags = conf.get("tags", [{}])[0] if isinstance(conf.get("tags"), list) else conf.get("tags")

        if not tags:
            return CheckResult.FAILED

        required_tags = ["Owner", "Environment", "CostCenter"]

        missing = [t for t in required_tags if t not in tags]

        if missing:
            return CheckResult.FAILED

        return CheckResult.PASSED


check = RequiredTagsCheck()