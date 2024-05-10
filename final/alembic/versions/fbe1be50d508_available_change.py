"""available-change

Revision ID: fbe1be50d508
Revises: 9e0d39f9bf1a
Create Date: 2024-05-09 23:33:06.506556

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'fbe1be50d508'
down_revision: Union[str, None] = '9e0d39f9bf1a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('availabilities', sa.Column('day_of_month', sa.Integer(), nullable=True))
    op.add_column('availabilities', sa.Column('month', sa.Integer(), nullable=True))
    op.add_column('availabilities', sa.Column('hour', sa.Integer(), nullable=True))
    op.drop_column('availabilities', 'end_time')
    op.drop_column('availabilities', 'start_time')
    op.drop_column('availabilities', 'day_of_week')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('availabilities', sa.Column('day_of_week', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('availabilities', sa.Column('start_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('availabilities', sa.Column('end_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('availabilities', 'hour')
    op.drop_column('availabilities', 'month')
    op.drop_column('availabilities', 'day_of_month')
    # ### end Alembic commands ###