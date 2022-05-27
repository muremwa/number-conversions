from .rec import find_recurring_pattern
from . import assure

ensure_no_base_10 = assure.ensure_no_base_10
ensure_base_is_standard = assure.ensure_base_is_standard
ensure_number_is_representable = assure.ensure_number_is_representable
base_limits = assure.ensure_number_representation_is_within_base_limits

__all__ = [
    'find_recurring_pattern',
    'ensure_no_base_10',
    'ensure_base_is_standard',
    'ensure_number_is_representable'
    'base_limits'
]