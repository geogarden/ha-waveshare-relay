"""Check localization coverage and stable formatting placeholders."""
import json
import re
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

from custom_components.waveshare_relay import entity as ent
from custom_components.waveshare_relay import select as select_mod
from custom_components.waveshare_relay import sensor as sensor_mod
from conftest import patch_ce

COMPONENT = Path(__file__).resolve().parents[1] / 'custom_components/waveshare_relay'


def leaves(value, prefix=''):
    if isinstance(value, dict):
        return {path: text for key, item in value.items()
                for path, text in leaves(item, f'{prefix}.{key}').items()}
    assert isinstance(value, str) and value.strip(), prefix
    return {prefix: value}


def test_polish_translation_matches_canonical_keys_and_placeholders():
    source = json.loads((COMPONENT / 'strings.json').read_text())
    polish = json.loads((COMPONENT / 'translations/pl.json').read_text())
    expected, translated = leaves(source), leaves(polish)
    assert expected.keys() == translated.keys()
    for key, value in expected.items():
        assert set(re.findall(r'{(\w+)}', value)) == set(re.findall(r'{(\w+)}', translated[key])), key


def test_english_fallback_matches_canonical_strings():
    assert json.loads((COMPONENT / 'strings.json').read_text()) == json.loads(
        (COMPONENT / 'translations/en.json').read_text())


def test_polish_channel_names_keep_identity_and_live_renames():
    coordinator = MagicMock()
    coordinator.relay_names = ['Garaż']
    entry = MagicMock(entry_id='e1')
    with patch.object(ent.CoordinatorEntity, '__init__', patch_ce):
        mode = select_mod.WaveshareChannelModeSelect(coordinator, entry, 0)
        duration = sensor_mod.WaveshareChannelDurationSensor(coordinator, entry, 0, 'ein')
    for entity, domain, key, label in (
        (mode, 'select', 'channel_mode', 'Tryb'),
        (duration, 'sensor', 'duration_ein', 'Czas włączenia'),
    ):
        entity.platform = MagicMock()
        entity.platform_data = SimpleNamespace(
            platform_name='waveshare_relay', domain=domain,
            platform_translations={f'component.waveshare_relay.entity.{domain}.{key}.name': label},
            component_translations={},
        )
        assert entity.name == f'Garaż {label}'
    assert mode.unique_id == 'e1_relay_1_mode'
    assert duration.unique_id == 'e1_ch1_ein_dauer'
    coordinator.relay_names[0] = 'Pompa'
    assert mode.name == 'Pompa Tryb'
    assert duration.name == 'Pompa Czas włączenia'
