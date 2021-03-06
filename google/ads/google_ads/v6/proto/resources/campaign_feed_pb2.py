# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v6/proto/resources/campaign_feed.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v6.proto.common import matching_function_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_common_dot_matching__function__pb2
from google.ads.google_ads.v6.proto.enums import feed_link_status_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_feed__link__status__pb2
from google.ads.google_ads.v6.proto.enums import placeholder_type_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_placeholder__type__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v6/proto/resources/campaign_feed.proto',
  package='google.ads.googleads.v6.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v6.resourcesB\021CampaignFeedProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V6.Resources\312\002!Google\\Ads\\GoogleAds\\V6\\Resources\352\002%Google::Ads::GoogleAds::V6::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n;google/ads/googleads_v6/proto/resources/campaign_feed.proto\x12!google.ads.googleads.v6.resources\x1a<google/ads/googleads_v6/proto/common/matching_function.proto\x1a:google/ads/googleads_v6/proto/enums/feed_link_status.proto\x1a:google/ads/googleads_v6/proto/enums/placeholder_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xd4\x04\n\x0c\x43\x61mpaignFeed\x12\x44\n\rresource_name\x18\x01 \x01(\tB-\xe0\x41\x05\xfa\x41\'\n%googleads.googleapis.com/CampaignFeed\x12\x38\n\x04\x66\x65\x65\x64\x18\x07 \x01(\tB%\xe0\x41\x05\xfa\x41\x1f\n\x1dgoogleads.googleapis.com/FeedH\x00\x88\x01\x01\x12@\n\x08\x63\x61mpaign\x18\x08 \x01(\tB)\xe0\x41\x05\xfa\x41#\n!googleads.googleapis.com/CampaignH\x01\x88\x01\x01\x12]\n\x11placeholder_types\x18\x04 \x03(\x0e\x32\x42.google.ads.googleads.v6.enums.PlaceholderTypeEnum.PlaceholderType\x12K\n\x11matching_function\x18\x05 \x01(\x0b\x32\x30.google.ads.googleads.v6.common.MatchingFunction\x12U\n\x06status\x18\x06 \x01(\x0e\x32@.google.ads.googleads.v6.enums.FeedLinkStatusEnum.FeedLinkStatusB\x03\xe0\x41\x03:i\xea\x41\x66\n%googleads.googleapis.com/CampaignFeed\x12=customers/{customer_id}/campaignFeeds/{campaign_id}~{feed_id}B\x07\n\x05_feedB\x0b\n\t_campaignB\xfe\x01\n%com.google.ads.googleads.v6.resourcesB\x11\x43\x61mpaignFeedProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V6.Resources\xca\x02!Google\\Ads\\GoogleAds\\V6\\Resources\xea\x02%Google::Ads::GoogleAds::V6::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads__v6_dot_proto_dot_common_dot_matching__function__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_feed__link__status__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_placeholder__type__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CAMPAIGNFEED = _descriptor.Descriptor(
  name='CampaignFeed',
  full_name='google.ads.googleads.v6.resources.CampaignFeed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.resources.CampaignFeed.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\372A\'\n%googleads.googleapis.com/CampaignFeed', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='feed', full_name='google.ads.googleads.v6.resources.CampaignFeed.feed', index=1,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\372A\037\n\035googleads.googleapis.com/Feed', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='campaign', full_name='google.ads.googleads.v6.resources.CampaignFeed.campaign', index=2,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\372A#\n!googleads.googleapis.com/Campaign', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='placeholder_types', full_name='google.ads.googleads.v6.resources.CampaignFeed.placeholder_types', index=3,
      number=4, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='matching_function', full_name='google.ads.googleads.v6.resources.CampaignFeed.matching_function', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v6.resources.CampaignFeed.status', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352Af\n%googleads.googleapis.com/CampaignFeed\022=customers/{customer_id}/campaignFeeds/{campaign_id}~{feed_id}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_feed', full_name='google.ads.googleads.v6.resources.CampaignFeed._feed',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_campaign', full_name='google.ads.googleads.v6.resources.CampaignFeed._campaign',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=371,
  serialized_end=967,
)

_CAMPAIGNFEED.fields_by_name['placeholder_types'].enum_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_placeholder__type__pb2._PLACEHOLDERTYPEENUM_PLACEHOLDERTYPE
_CAMPAIGNFEED.fields_by_name['matching_function'].message_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_common_dot_matching__function__pb2._MATCHINGFUNCTION
_CAMPAIGNFEED.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_feed__link__status__pb2._FEEDLINKSTATUSENUM_FEEDLINKSTATUS
_CAMPAIGNFEED.oneofs_by_name['_feed'].fields.append(
  _CAMPAIGNFEED.fields_by_name['feed'])
_CAMPAIGNFEED.fields_by_name['feed'].containing_oneof = _CAMPAIGNFEED.oneofs_by_name['_feed']
_CAMPAIGNFEED.oneofs_by_name['_campaign'].fields.append(
  _CAMPAIGNFEED.fields_by_name['campaign'])
_CAMPAIGNFEED.fields_by_name['campaign'].containing_oneof = _CAMPAIGNFEED.oneofs_by_name['_campaign']
DESCRIPTOR.message_types_by_name['CampaignFeed'] = _CAMPAIGNFEED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CampaignFeed = _reflection.GeneratedProtocolMessageType('CampaignFeed', (_message.Message,), {
  'DESCRIPTOR' : _CAMPAIGNFEED,
  '__module__' : 'google.ads.googleads_v6.proto.resources.campaign_feed_pb2'
  ,
  '__doc__': """A campaign feed.
  
  Attributes:
      resource_name:
          Immutable. The resource name of the campaign feed. Campaign
          feed resource names have the form:  \`customers/{customer\_id}
          /campaignFeeds/{campaign\_id}~{feed\_id}
      feed:
          Immutable. The feed to which the CampaignFeed belongs.
      campaign:
          Immutable. The campaign to which the CampaignFeed belongs.
      placeholder_types:
          Indicates which placeholder types the feed may populate under
          the connected campaign. Required.
      matching_function:
          Matching function associated with the CampaignFeed. The
          matching function is used to filter the set of feed items
          selected. Required.
      status:
          Output only. Status of the campaign feed. This field is read-
          only.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.resources.CampaignFeed)
  })
_sym_db.RegisterMessage(CampaignFeed)


DESCRIPTOR._options = None
_CAMPAIGNFEED.fields_by_name['resource_name']._options = None
_CAMPAIGNFEED.fields_by_name['feed']._options = None
_CAMPAIGNFEED.fields_by_name['campaign']._options = None
_CAMPAIGNFEED.fields_by_name['status']._options = None
_CAMPAIGNFEED._options = None
# @@protoc_insertion_point(module_scope)
