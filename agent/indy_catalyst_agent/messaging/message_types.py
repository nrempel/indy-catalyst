from enum import Enum

class MessageTypes(Enum):
    # Admin Base Messages
    ADMIN_BASE_STATE_REQUEST = "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/admin/1.0/state_request"
    ADMIN_BASE_STATE = "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/admin/1.0/state"

    # Admin Wallet Connection Messages
    ADMIN_WALLET_CONNECTION_CONNECT = "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/admin_walletconnection/1.0/connect"

    # Admin Connection Messages
    ADMIN_CONNECTION_GENERATE_INVITE = "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/admin_connections/1.0/generate_invite"
    ADMIN_CONNECTION_INVITE_GENERATED = "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/admin_connections/1.0/invite_generated"

    # Connection Messages
    # CONNECTION_INVITATION = "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/connections/1.0/invitation"
    CONNECTION_INVITE = "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/connections/1.0/invite"
    CONNECTION_REQUEST = "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/connections/1.0/request"
    CONNECTION_RESPONSE = "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/connections/1.0/response"

    # Credential Messages
    CREDENTIAL_OFFER = "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/connections/1.0/credential_offer"
    CREDENTIAL_REQUEST = "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/connections/1.0/credential_request"
    CREDENTIAL = "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/connections/1.0/credential"
    
    # Proof Messages
    PROOF_REQUEST = "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/connections/1.0/proof_request"
    PROOF = "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/connections/1.0/disclosed_proof"

    # Routing Messages
    FORWARD = "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/routing/1.0/forward"