import pytest
from src.log_parser import parse_log_line

def test_method():
    c = parse_log_line("2026-09-25 10:02:11 ERROR payment-service Database connection failed")
    assert type(c) == dict
    assert c.get('level') == 'ERROR'
    
def test_log_parse_log_line_invalid():
    d= parse_log_line("INVALID")
    assert d == None
    
def test_log_parse_service_name():
    dict_log_line = parse_log_line("2026-09-25 10:02:11 ERROR payment-service Database connection failed")
    assert dict_log_line.get("service") == "payment-service"