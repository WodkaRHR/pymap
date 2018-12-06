import agb.types
from functools import partial

person_type = agb.types.Structure([
    ('target_index', 'u8'),
    ('picture', 'u8'),
    ('field_2', 'u8'),
    ('field_3', 'u8'),
    ('x', 's16'),
    ('y', 's16'),
    ('level', 'u8'),
    ('behaviour', 'u8'),
    ('behaviour_range', 'u8'),
    ('field_B', 'u8'),
    ('is_trainer', 'u8'),
    ('field_D', 'u8'),
    ('alert_radius', 'u16'),
    ('script', 'ow_script_pointer'),
    ('flag', 'u16'),
    ('field_16', 'u16')
])

trigger_type = agb.types.Structure([
    ('x', 's16'),
    ('y', 's16'),
    ('level', 'u8'),
    ('field_5', 'u8'),
    ('var', 'u16'),
    ('value', 'u16'),
    ('field_A', 'u8'),
    ('field_B', 'u8'),
    ('script', 'ow_script_pointer')
])

warp_type = agb.types.Structure([
    ('x', 's16'),
    ('y', 's16'),
    ('level', 'u8'),
    ('target_warp_idx', 'u8'),
    ('target_map', 'u8'),
    ('target_bank', 'u8')
])

signpost_item_type = agb.types.BitfieldType('u32', [
    ('item', None, 16),
    ('flag', None, 8),
    ('amount', None, 8)
])

signpost_value_type = agb.types.UnionType({
        'item' : 'event.signpost_item',
        'script' : 'ow_script_pointer'
    },
    lambda project, context, parents: 'script' if parents[-1]['type'] < 5 else 'item'
)

signpost_type = agb.types.Structure([
    ('x', 's16'),
    ('y', 's16'),
    ('level', 'u8'),
    ('type', 'u8'),
    ('field_6', 'u8'),
    ('field_7', 'u8'),
    ('value', 'event.signpost_value')
])

person_array_type = agb.types.VariableSizeArrayType(
    'event.person',
    (1, ['person_cnt'])
)

warp_array_type = agb.types.VariableSizeArrayType(
    'event.warp',
    (1, ['warp_cnt'])
)

trigger_array_type = agb.types.VariableSizeArrayType(
    'event.trigger',
    (1, ['trigger_cnt'])
)

signpost_array_type = agb.types.VariableSizeArrayType(
    'event.signpost',
    (1, ['signpost_cnt'])
)

person_array_pointer_type = agb.types.PointerType(
    'event.person_array',
    # The label is always persons, 2-aligned, and not global
    (lambda project, context, parents: ('persons', 2, False))
)

warp_array_pointer_type = agb.types.PointerType(
    'event.warp_array',
    # The label is always warps, 2-aligned, and not global
    (lambda project, context, parents: ('warps', 2, False))
)

trigger_array_pointer_type = agb.types.PointerType(
    'event.trigger_array',
    # The label is always triggers, 2-aligned, and not global
    (lambda project, context, parents: ('triggers', 2, False))
)

signpost_array_pointer_type = agb.types.PointerType(
    'event.signpost_array',
    # The label is always signposts, 2-aligned, and not global
    (lambda project, context, parents: ('signposts', 2, False))
)

event_header_type = agb.types.Structure([
    ('person_cnt', 'u8'),
    ('warp_cnt', 'u8'),
    ('trigger_cnt', 'u8'),
    ('signpost_cnt', 'u8'),
    ('persons', 'event.person_array_pointer'),
    ('warps', 'event.warp_array_pointer'),
    ('triggers', 'event.trigger_array_pointer'),
    ('signposts', 'event.signpost_array_pointer')
])

# These model declarations will be exported

default_model = {
    'event.person' : person_type,
    'event.warp' : warp_type,
    'event.trigger' : trigger_type,
    'event.signpost' : signpost_type,
    'event.signpost_item' : signpost_item_type,
    'event.signpost_value' : signpost_value_type,
    'event.person_array' : person_array_type,
    'event.warp_array' : warp_array_type,
    'event.trigger_array' : trigger_array_type,
    'event.signpost_array' : signpost_array_type,
    'event.person_array_pointer' : person_array_pointer_type,
    'event.warp_array_pointer' : warp_array_pointer_type,
    'event.trigger_array_pointer' : trigger_array_pointer_type,
    'event.signpost_array_pointer' : signpost_array_pointer_type,
    'event.event_header' : event_header_type
}