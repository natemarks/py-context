#!/usr/bin/env python3
"""example test file


"""
import pytest
from src.show_env import print_python_info
# from tests.helper import (
#     case_data_path,
#     update_data_file,
#     read_json_data_file,
# )

@pytest.mark.unit
def test_dummy():
    assert True


@pytest.mark.unit
def test_print_env():
    print_python_info()
    assert True

# @pytest.mark.unit
# @pytest.mark.parametrize(
#     "environment",
#     [
#         pytest.param("dev", id="dev"),
#         pytest.param("integration", id="integration"),
#         pytest.param("staging", id="staging"),
#         pytest.param("production", id="production"),
#     ],
# )
# def test_activegate_stack_actual(request, environment, update_golden):
#     """test biometric aware wiht actual environment data
#
#     use the live data in config/dev, config/staging and config/production
#
#     """
#     # use stack input data from actual environments
#     input_path = get_actual_path(environment)
#     # test_data path for case
#     data_path = case_data_path(request)
#     a_input = AppVpcInput.from_config_directory(input_path)
#     ag_input = ActivegateInput.from_config_directory(input_path)
#
#     app = App()
#
#     av_stk = AppVpcStack(
#         scope=app,
#         cdk_env=Environment(),
#         s_input=a_input,
#     )
#
#     stk = ActivegateStack(
#         scope=app,
#         cdk_env=Environment(),
#         s_input=ag_input,
#         app_vpc_stack=av_stk,
#     )
#
#     template = assertions.Template.from_stack(stk)
#     if update_golden:
#         update_data_file(
#             data_path,
#             "expected.json",
#             json.dumps(template.to_json(), indent=2),
#         )
#
#     template.template_matches(read_json_data_file(data_path, "expected.json"))