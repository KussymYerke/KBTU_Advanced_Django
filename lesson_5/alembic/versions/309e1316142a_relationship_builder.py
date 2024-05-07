"""relationship builder

Revision ID: 309e1316142a
Revises: 40a151b8e643
Create Date: 2024-05-04 10:50:34.520260

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '309e1316142a'
down_revision: Union[str, None] = '40a151b8e643'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('presidents', sa.Column('country_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'presidents', 'countries', ['country_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'presidents', type_='foreignkey')
    op.drop_column('presidents', 'country_id')
    # ### end Alembic commands ###